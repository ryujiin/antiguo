Loviz.Views.Login = Backbone.View.extend({
	className:'bloque',
	template: swig.compile($("#login_template").html()),	
	events: {
		'submit': 'logearse',
	},
	initialize : function () {
		this.render();
	},
	render:function () {
        var html = this.template();
        this.$el.html(html);
	},
	logearse:function (e) {
		e.preventDefault();
		var email = this.$('input[type=email]');
		var pass = this.$('input[type=password]');
		if (email.val()!=='') {
			if (pass.val()!=='') {
				this.$el.fadeOut();
				this.login(email.val(),pass.val());
			}else{
				pass.addClass('fallo');
				this.$('.pass .text_help').empty().addClass('text_fallo').append('<span class="icon-cross2"> Este campo es necesario')
			}
		}else{
			email.addClass('fallo');
			this.$('.email .text_help').empty().addClass('text_fallo').append('<span class="icon-cross2"> Este campo es necesario')
		}
	},
	login:function (email,pass) {
		var self = this;
		$.post('/ajax/login/',{username : email, password :pass})
		.done(function (data) {
			self.datos_user();
      		window.routers.base.navigate('/perfil/', {trigger:true});
      		$("#usuario").removeClass('page_loading');
		})
		.fail(function () {
			self.$el.fadeIn();
			$('#formu_login .ayuda_form .text_help').empty().addClass('text_fallo').append('<span class="icon-cross2">El usuario o la contraseña no son correctos');
			$('#usuario').removeClass('page_loading');
			$( "#formu_login input" ).each(function() {
				$(this).val('');
			});
		})
	},
	datos_user:function () {
		window.models.usuario.buscar_usuario();
		var carro_nuevo = new Loviz.Models.Carro();
		carro_nuevo.fetch().done(function () {
			carro_nuevo.fucionar_carro();
		})
	},
});
