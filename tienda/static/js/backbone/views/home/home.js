Loviz.Views.Home = Backbone.View.extend({
	el:$("#home"),
	events: {
	},
	initialize : function () {
		var self = this;
		window.routers.base.on('route',function(e){
			self.aparecer(e);		
		});
		window.routers.catalogo.on('route',function(e){
			self.aparecer(e);		
		});
		this.landing_nuevos_productos = new Loviz.Views.Landing_nuevos_productos();
    	this.slider_novedades = new Loviz.Views.Slider_home($('#novedades'));
    	this.slider_ofertas = new Loviz.Views.Slider_home($('#oferta'));
    	this.redes = new Loviz.Views.Redes_sociales();
	},
	aparecer:function (e) {
		if (e === 'root') {
			this.$el.show();
		}else{
			this.$el.hide();
		}
	}
});
