Loviz.Views.Suscribcion = Backbone.View.extend({
	el:$('#suscripcion'),
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
	},
	aparecer:function (e) {
		if (e === 'root') {
			this.$el.removeClass('no_home');
		}else{
			this.$el.addClass('no_home');
		}
	},
});
