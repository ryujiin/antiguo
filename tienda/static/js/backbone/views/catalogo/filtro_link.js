Loviz.Views.Filtro_link = Backbone.View.extend({
    tagName: 'li',
    events: {
        'click' : 'activo'
    },
    template: swig.compile($("#catalogo_filtro_link_template").html()),
    
    initialize: function () {
        this.activado=false;
    },
    render: function () {
        var album = this.model.toJSON()
        var html = this.template(album);
        this.$el.html(html);
        return this;
    },
    activo:function () {
        if (this.activado===false) {
            this.$('span').addClass('icon-square-check').removeClass('icon-stop')
            this.activado=true;
        }else{
            this.$('span').addClass('icon-stop').removeClass('icon-square-check')
            this.activado=false;
        }
    }
});