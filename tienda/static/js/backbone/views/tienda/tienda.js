Loviz.Views.Tienda = Backbone.View.extend({
	events: {
		'click .link':'link_intero',
	},
	initialize : function ($el) {
		var self = this;
		this.$el = $el;
	},
	link_intero:function (e) {
		e.preventDefault();
		var link = e.currentTarget.pathname;
		
		window.routers.base.navigate(link, {trigger:true});
	}
});
