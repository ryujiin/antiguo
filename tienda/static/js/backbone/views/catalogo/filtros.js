Loviz.Views.CajaFiltros = Backbone.View.extend({
    className: 'bloque',
    events: {
    },
    template: swig.compile($("#catalogo_filtro_template").html()),
    
    initialize: function () {
        this.render();
        this.collection.fetch();
        this.listenTo(this.collection, "add", this.add_filtro, this);
    },
    render: function () {
        var json_filtro = {'titulo':this.collection.filtro}
        var html = this.template(json_filtro);
        this.$el.html(html);
        $('#catalogo .lateral_menu').append(this.$el);
    },
    add_filtro:function (filtro) {
        var link = new Loviz.Views.Filtro_link({ model: filtro });
        this.$('ul').append(link.render().el);
    }
});