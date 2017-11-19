% rebase('base.tpl')

<h2>Nammi</h2>
<div>
    % for i in range(len(products)):
       <p> <a href="/cart/add/{{ products[i]["pid"] }}"> {{ products[i]["name"] }} </a> </p>
    % end
    <p>Fjöldi heimsókna: {{teljari}}</p>
    <p><a href="/cart">Karfa</a></p>
</div>
