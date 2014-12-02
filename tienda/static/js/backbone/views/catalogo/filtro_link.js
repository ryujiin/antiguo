Loviz.Views.Filtro_link = Backbone.View.extend({
    tagName: 'li',
    events: {
        'click' : 'activo'
    },
    template: swig.compile($("#catalogo_filtro_link_template").html()),
    
    initialize: function () {
        var self = this;
        this.activado=false;
        window.routers.catalogo.on('route:catalogo',function(){
            self.desactivar();
        })
    },
    render: function () {
        var album = this.model.toJSON()
        var html = this.template(album);
        this.$el.html(html);
        return this;
    },
    activo:function () {
        if (this.activado===false) {
            debugger;
            this.$('span').addClass('icon-square-check').removeClass('icon-stop')
            this.activado=true;
            this.filtro_etiqueta = new Loviz.Views.Filtro_Etiqueta({model:this.model})
            debugger;
        }else{
            this.desactivar();
        }
    },
    desactivar:function  () {
        this.$('span').addClass('icon-stop').removeClass('icon-square-check')
        this.activado=false;
        if (this.filtro_etiqueta) {
            this.filtro_etiqueta.remove();
        };

    }
});