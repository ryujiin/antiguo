Loviz.Views.Menu_principal = Backbone.View.extend({
	el:$("#menu_principal"),
	events: {
	},
	initialize : function () {
		var self = this;
		var menu_offset = this.$el.offset();

		$(window).on('scroll', function() {
			if($(window).scrollTop() > menu_offset.top) {
				self.$el.addClass('fijo');
			} else {
				self.$el.removeClass('fijo');
			}
		});
		this.cargar_links();
	},
	cargar_links:function () {
		var self = this;
		this.coleccionLink = new Loviz.Collections.Menu_principal();
		this.coleccionLink.fetch().done(function () {
    		self.coleccionLink.forEach(self.addOne, self);			
		})
	},
	addOne:function (link) {
		var link_views = new Loviz.Views.Menu_principal_link({ model: link });
    	this.$('.menu').append(link_views.render().el);
	}
});
