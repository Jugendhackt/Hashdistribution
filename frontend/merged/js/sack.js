var node = [], edges = [], url_local = "data/hashtag.json";
$.getJSON(url_local, function (a) {
    node.push({id: 9999, label: a.ht});
    for (var b = 0; b < a.childs.length; ++b) {
        node.push({id: b, label: a.childs[b].ht, title: a.childs[b].count}), edges.push({
            from: 9999,
            to: b,
            value: a.childs[b].count / 2,
            label: a.childs[b].count
        });
        for (var c = 0; c < a.childs[b].childs.length; c++)node.push({
            id: 10 * b + c + 50,
            label: a.childs[b].childs[c].ht,
            title: a.childs[b].childs[c].count
        }), edges.push({
            from: b,
            to: 10 * b + c + 50,
            value: a.childs[b].childs[c].count / 2,
            label: a.childs[b].childs[c].count
        })
    }
    var d = document.getElementById("graph"), e = {
        nodes: new vis.DataSet(node),
        edges: new vis.DataSet(edges)
    }, f = {nodes: {shape: "dot"}};
    new vis.Network(d, e, f)
});