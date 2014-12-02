Loviz.Views.Menu_principal_link = Backbone.View.extend({
	tagName:'li',
	template: swig.compile($("#menu_principal_link_template").html()),
	events: {
	},
	initialize : function () {
	},
	render : function () {
		var album = this.model.toJSON()
        var html = this.template(album);
        this.$el.html(html);
        return this;
	}
});
