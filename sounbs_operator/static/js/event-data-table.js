$(document).ready(function () {
    var columns = []; // array
    var response = null;
            
            $('#btn-show-collar').click(function () {                              
                $('#collar').DataTable({
                    "processing": true,
                    "serverSide": true,  
                    "ajax": function (data, callback, settings) {
                        $.ajax({
                            url: '/HO/DrillHole/CollarGetAll',
                            type: 'POST',
                            data: data,
                            success: function (data) {                               
 
                                response = data.data;
 
                                $.each(response[0], function (key, value) {
                                    var my_item = {};                                  
                                    my_item.title = key;
                                    my_item.data = key;
                                    columns.push(my_item);
 
                                });
 
                                //console.log(response);
                                callback(data);                               
                            }
                        })
                    },                                    
                    "data": response,                    
                    "columns": columns
 
                });                        
                
 
            });
}