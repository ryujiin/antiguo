Loviz.Views.Landing = Backbone.View.extend({
	el:$('#landing_page'),
	events: {
	},
	initialize : function () {
		var self = this;
		this.crear_banners();
		this.crear_nuevos();
		window.routers.base.on('route',function(e){
			self.aparecer(e);
		});
		window.routers.catalogo.on('route',function(e){
			self.aparecer(e);
		});

	},
	aparecer : function (e) {
		if (e === 'landing') {
			this.$el.show();
		}else{
			this.$el.hide();
		}
	},
	crear_banners:function () {
		debugger;
		this.$('.banners').empty();
		this.banners = window.collections.categorias.where({genero_slug:window.app.landing});
		this.clase_responsive();
		this.banners.forEach(this.addBanner,this);
	},
	addBanner:function (banner) {
		var banner_view = new Loviz.Views.Landing_Banner_cate({model:banner});
		this.$('.banners').append(banner_view.render().el);
		banner_view.$el.addClass(this.banner_clase);
		
	},
	clase_responsive:function () {
		var num = this.banners.length;
		if (num == 2 ) {
			this.banner_clase = 'col-md-6'
		}else if(num == 3){
			this.banner_clase = 'col-md-4'			
		}else if (num == 4) {
			this.banner_clase = 'col-md-3'
		};
	},
	crear_nuevos:function () {
		if (true) {};
	}
});
