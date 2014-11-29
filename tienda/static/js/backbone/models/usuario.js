Loviz.Models.Usuario = Backbone.Model.extend({
	url:'/api/cliente/perfil/',
	name:'perfil',
	initialize:function () {
		this.buscar_usuario();
	},
	buscar_usuario:function () {
		var self=this;
		this.fetch()
		.done(function () {
			$.sessionStorage.set('usuario',self.id);
		}).fail(function () {
			self.set('texto','no hay usuario')
		})
	}
});