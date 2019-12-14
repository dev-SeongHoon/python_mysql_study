create table sale_detail (
    no int(11) not null,
    sale_price int(11) not null,
    addTax int(11) not null,
    supply_price int(11) not null,
    margin_price int(11) not null,
    foreign key(no) references sale(no) on delete cascade
);

delimiter $$
create trigger tri_sale_insert_after_detail
after insert on sale
for each row
begin
    set @saleprice = new.price * new.saleCnt,
    @addtax = ceil(@saleprice / 11),
    @supprice = @saleprice - @addtax,
    @marPrice = round(@supprice * (new.marginRate / 100));

    insert into sale_detail(no, sale_price, addTax, supply_price, margin_price)
        values(new.no, @saleprice, @addtax, @supprice, @marPrice);
end $$
delimiter ;

drop trigger tri_sale_insert_after_detail;

delimiter $$
create trigger tri_sale_update_after_detail
after update on sale
for each row
begin
    set @saleprice = new.price * new.saleCnt,
    @addtax = ceil(@saleprice / 11),
    @supprice = @saleprice - @addtax,
    @marPrice = round(@supprice * (new.marginRate / 100));

    update coffee_pjt.sale_detail
        set sale_price=@saleprice, addTax=@addtax, supply_price=@supprice, margin_price=@marPrice
      where no = new.no;
end $$
delimiter ;

drop trigger tri_sale_update_after_detail;


drop procedure if exists proc_saledetail_orderby;
delimiter $$
create procedure proc_saledetail_orderby (in isSalePrice boolean)
    begin
        if isSalePrice then
            select (select count(*)+1 from sale_detail s2 where s2.sale_price > s1.sale_price) rank,
                sale.code code, p.name name, price, saleCnt, supply_price, addTax,
                sale_price, marginRate, margin_price
              from sale inner join sale_detail s1 on sale.no = s1.no join product p on sale.code = p.code order by rank;
        else
            select (select count(*)+1 from sale_detail s2 where s2.margin_price > s1.margin_price) rank,
                sale.code code, p.name name, price, saleCnt, supply_price, addTax,
                sale_price, marginRate, margin_price
              from sale inner join sale_detail s1 on sale.no = s1.no join product p on sale.code = p.code order by rank;
        end if;
    end $$
    delimiter ;