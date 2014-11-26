Loviz.Views.Crear_User = Backbone.View.extend({
	className:'bloque',
	template: swig.compile($("#crear_user_template").html()),	
	events: {
		'click .aparecer': 'aparecer_formu',
		'blur #pass2_crear':'verificar_contra',		
		'submit': 'crear_cuenta',
	},
	initialize : function () {
		this.render();
	},
	render:function () {
        var html = this.template();
        this.$el.html(html);
	},
	aparecer_formu:function (e) {
		var div = $(e.currentTarget);
		div.fadeOut();
		this.$("#formu_crear_cuenta").fadeIn();
	},
	verificar_contra:function (e) {
		var div = $(e.currentTarget);
		var valor1=$("#formu_crear_cuenta #pass_crear").val();
		var valor2=$("#formu_crear_cuenta #pass2_crear").val();
		var conte_ayuda  = $('.'+e.currentTarget.id+' .text_help');
		if (valor1!==valor2) {
			var texto_ayuda = '<span class="icon-cross2">Las contraseñas no son iguales' 
			this.dato_fallo(div,conte_ayuda,texto_ayuda)
			div.val('');
		}
	},
	crear_cuenta:function (e) {
		var self=this;
		e.preventDefault();
		var email = $('#formu_crear_cuenta #email_crear')
		var pass = $('#formu_crear_cuenta #pass_crear')
		var pass2 = $('#formu_crear_cuenta #pass2_crear')
		if (email.val()!=='') {
			if (pass.val()!=='') {
				if (pass.val()===pass2.val()) {
					//comenzar efecto
					this.$el.fadeOut();
					$('#usuario').addClass('page_loading');
					$.post('https://lovizdc.herokuapp.com/api/usuario/',{username : email.val(), password :pass.val(),email:email.val()})
					.done(function (data) {
						window.views.ingresar.login_view.login(email.val(),pass.val());
					})
					.fail(function () {
						self.$el.fadeIn();
						$('#formu_crear_cuenta .ayuda_form .text_help').empty().addClass('text_fallo').append('<span class="icon-cross2">El usuario ya existe en nuestro sistema');
						$('#usuario').removeClass('page_loading');
						email.val('');
						pass.val('');
						pass2.val('');
					})
				}else{
					pass.addClass('fallo');
					pass2.addClass('fallo');
					$('#formu_crear_cuenta .pass2_crear .text_help').empty().addClass('text_fallo').append('<span class="icon-cross2">Las contraseñas no son iguales')
				}
			}else{
				pass.addClass('fallo');
				$('#formu_crear_cuenta .pass_crear .text_help').empty().addClass('text_fallo').append('<span class="icon-cross2"> Este campo es necesario')
			}
		}else{
			email.addClass('fallo');
			$('#formu_crear_cuenta .email_crear .text_help').empty().addClass('text_fallo').append('<span class="icon-cross2"> Este campo es necesario')
		}	
	},
	
});
