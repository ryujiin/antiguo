Loviz.Models.Usuario = Backbone.Model.extend({
	url:'/api/cliente/perfil/',
	name:'perfil',
	initialize:function () {
		this.buscar_usuario();
	},
	buscar_usuario:function () {
		var self = this;
		var usuario = $.sessionStorage.get('usuario');
		var token = $.sessionStorage.get('token_login');
		this.fetch()
		.fail(function () {
			if (usuario && token) {
				this.fetch({headers:{'Authorization':'JWT '+token}})
			};
		}).done(function () {
			$.sessionStorage.set({'usuario':self.id,'token_login':'usuarioLogin'})
		})
	}
});