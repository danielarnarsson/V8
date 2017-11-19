% rebase('base.tpl')

<h1>Karfa</h1>

<div>
    <!-- athugum hvort karfa sé tóm -->
    % if len(karfa) <= 0:
        <p>Það eru engar vörur í körfu</p>
        <p><a href="/">Versla meira</a></p>
    <!-- birtum vörur í körfu -->
    % else:
        % for i in range(len(karfa)):
            <p> {{ karfa[i] }} <p>
        % end
    <p><a href="/">Versla meira</a></p>

    <!-- tæmum körfu, eyðum öllu sessins-->
    <p><a href="/cart/remove">Fjarlægja allar vörur úr körfu</a></p>
    <p>{{info}}</p>
</div>
