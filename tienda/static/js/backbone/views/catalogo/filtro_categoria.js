Loviz.Views.Cate_CajaFiltros = Backbone.View.extend({
    className: 'bloque',
    events: {
    },
    template: swig.compile($("#catalogo_filtro_template").html()),
    
    initialize: function () {
        this.listenTo(this.collection, "add", this.add_filtro, this);
    },
    render: function () {
        var json_filtro = {'titulo': 'para '+this.genero}
        var html = this.template(json_filtro);
        this.$el.html(html);
        $('#catalogo .categorias').append(this.$el);
    },
    add_filtro:function (filtro) {
        if (filtro.toJSON().genero === this.genero) {
            var link = new Loviz.Views.Filtro_link({ model: filtro });
            link.model.set('filtro',true);
            this.$('ul').append(link.render().el);  
        };
    },
});