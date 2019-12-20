function getToken(){
    return document.getElementsByName('csrfmiddlewaretoken')[0].value;
}

function request (contexto) {    
    const data = Object.assign({ csrfmiddlewaretoken: contexto.token }, contexto.data || {});
    $.ajax({
        type: contexto.type,
        url: contexto.url,
        data: data,
        success: contexto.callBack,
        error: function(error){
            console.log(error);
        }
    })
}

function compensarHoraExtra(id){    
    const contexto = {};
    contexto.url = `/horas-extras/compensar-hora-extra/${id}/`;
    contexto.token = getToken();
    contexto.type = 'POST';
    contexto.callBack = function({mensagem, horas}){
        $('#mensagem').text(mensagem);
        $('#horas_atualizadas').text(`Quantidade de Horas: ${horas}`);
    }
    request(contexto);
    return false
}