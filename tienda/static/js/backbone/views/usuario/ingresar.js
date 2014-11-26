Loviz.Views.Ingresar= Backbone.View.extend({
	el:$("#ingresar"),
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

		this.login_view=new Loviz.Views.Login();
		this.crear_user_view=new Loviz.Views.Crear_User();
		this.$('#login').append(this.login_view.$el);
		this.$('#crear_user').append(this.crear_user_view.$el);
	},
	aparecer:function (e) {
		if (e === 'ingresar') {
			this.$el.show();
		}else{
			this.$el.hide();
		}
	},	
});
