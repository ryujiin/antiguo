Loviz.Views.Filtro_Etiqueta = Backbone.View.extend({
    tagName: 'span',
    events: {
    },
    template: swig.compile($("#filtro_etiqueta_template").html()),
    
    initialize: function () {
        this.render();
    },
    render: function () {
        var album = this.model.toJSON()
        var html = this.template(album);
        this.$el.html(html);
        window.views.catalogo_contenedor.$('.filtros').append(this.$el);
    },
});