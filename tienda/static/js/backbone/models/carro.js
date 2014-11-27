Loviz.Models.Carro = Backbone.Model.extend({
	urlRoot : '/api/carro/',
	name : 'Carro',
    url : function() {
        var base = this.urlRoot;
        if (this.isNew()) return base;
        return base + (base.charAt(base.length - 1) == '/' ? '' : '/') + this.id+'/';
    },
	initialize : function () {
		this.crear_carromodel();
	},
    defaults:{
        "propietario": null, 
        "estado": "Abierto", 
        "sesion_carro": "", 
        "lineas": 0, 
        "total": "0.00", 
        "subtotal": "0.00", 
        "envio": 0
    },
	crear_carromodel:function () {
		var self = this;
        var token = $.sessionStorage.get('token_login')
        var carro_local = $.sessionStorage.get('carro_local')
        var usuario = $.sessionStorage.get('usuario');
        debugger;
        
/*
        if (token) {
            self.fetch({
            	headers:{'Authorization':'JWT '+token}
            })
            .fail(function () {
                self.set('propietario',usuario);
            })
        }else if(carro_local){
            self.set('id',carro_local);
            self.fetch();
        }else{
            self.fetch({
                data:$.param({session:galleta})
            }).fail(function () {
                self.set('sesion_carro',galleta);              
            }).done(function (data) {
                $.sessionStorage.set(carro_local,data.id);
            })
        }
        */
    },
    saber_que_carro:function(){
        var usuario = $.sessionStorage.get('usuario');
        var token = $.sessionStorage.get('token_login')
    	if (window.models.carro !== this) {
            if (this.toJSON().lineas !==0 ) {
                var self = this;
                var nueva_collecion = new Loviz.Collections.Lineas();
                nueva_collecion.fetch({
                    data:$.param({carro:this.id})
                })
                .done(function () {
                    nueva_collecion.forEach(function (linea) {
                        linea.set('carro',window.models.carro.id);
                        linea.save();
                    });
                    self.set('estado','Fusionada');
                    self.save().done(function () {
                        window.models.carro.set('propietario',usuario)
                        window.models.carro.save();
                    });                    
                });
            }else{
                window.models.carro.set({'propietario':usuario,'estado':'Abierto'});
                this.set('estado','Fusionada');
                this.save().done(function () {
                    window.models.carro.save();
                    
                });
            }
    	};
    },
    salvar_primera:function () {
        if (this.id===undefined) {
            this.save().done(function (data) {
                $.sessionStorage.set('carro_local',data.id);
            })
        };
    }
});