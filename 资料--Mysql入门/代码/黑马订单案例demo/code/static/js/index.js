
$(function () {
           
            // 表头标签
            var sheetTitle = '<tr class="sheetTitle"><th>编号</th><th>网站/软件</th><th>账号</th><th>密码</th><th>备注</th><th>等级</th><th>创建时间</th></tr>'
            
            // 1. 数据标签
            function fnDataElementTr(data) {

                var dataTr = '<tr>' 
                                + '<td class="idInput"><input type="text" value=' + data.id +'></td>'
                                + '<td><input type="text" value=' +data.count+'></td>'
                                + '<td><input type="text" value=' +data.price+'></td>'
                                + '<td><input type="text" value=' +data.freight+'></td>'
                                + '<td><input type="text" value=' +data.user+'></td>'
                                + '<td>' +
                                        '<input list="browsers" type="text" value=' +data.status+'>' +
                                        '<datalist id="browsers">' +
                                              '<option value="有限时间">' +
                                              '<option value="永久">' +
                                              '<option value="SVIP">' +
                                        '</datalist>'+
                                    '</td>'
                                + '<td><input type="date" value=' +data.time+'></td>'
                                + '<td class="del"><input  type="button" value=" 删 除 "></td>'
                                + '<td class="update"><input type="button" value=" 修 改 "></td>'
                                + '</tr>'
                    
                return dataTr
                
            }
            
            // 1.首页初始化加载数据
            function fnLoadHomeData(judage) {
                $.get({
                    url:"/orders.html",
                    dataType:'json',
                    success:function (data) {
                        content = sheetTitle
                        for (let index = 0; index < data.length; index++) {
                            var dat = data[index];
                             //  1. 拼接数据
                           content += fnDataElementTr(dat)  
                        }
                       // 2. 插入数据
                       $('.orderlist').html(content)
                        
                       if (judage == "del") {
                        $('.del').show()
                       } else if (judage == "update") {
                        $('.update').show()  
                       }
                       $('.idInput').on('focus',function () {
                           alert('2332')
                        $(this).blur()
                    }) 
                       }

                   });
            }
            fnLoadHomeData()
            
            // 1.左侧操作按钮的 交互点击
            var $leftBtns = $('button');
            $leftBtns.click(function () {
                $(this).addClass('leftbtn').parent().siblings().children().removeClass('leftbtn');
            });
                    

            //  查询图书按钮 获取所有的图书信息展示
            $('.checkorder').click(function () {
               
                $('.orderlist').show()
                $('.addlist').hide()
                $('.del').hide()
                $('.update').hide()
               
            })  
            
            //  增加图书按钮 
            $('.addorder').click(function () {
                $('.orderlist').hide()
                $('.addlist').show()
                // 监听增加按钮
                $('.add').on('click',function () {
                    var addTds = $('.addlist input')
                    dict_data = {}
                    for (var i=0;i < (addTds.length-1); i++){
                        if (i==0) {
                            dict_data.id = 0
                        } else if(i==1){
                            dict_data.count = addTds.eq(i).val()
                        }else if(i==2){
                            dict_data.price = addTds.eq(i).val()
                        }else if(i==3){
                            dict_data.freight = addTds.eq(i).val()
                        }else if(i==4){
                            dict_data.user = addTds.eq(i).val()
                        }else if(i==5){
                            dict_data.status = addTds.eq(i).val()
                        }else if(i==6){
                            dict_data.time = addTds.eq(i).val()
                        }
                    }
                    if (dict_data.count == ""|dict_data.price == ""|dict_data.freight == ""|dict_data.user == ""|dict_data.status == ""|dict_data.time == "") {
                        alert('输入内容不能为空!')
                        return
                    }
                    $.post({
                        url:"/add_order.html",
                        dataType:"json",
                        data:JSON.stringify(dict_data),
                        success:function (dat) {
                            alert(dat.data)
                        }
                    })
                    // 清空所有 输入框!
                    for (var i=0;i < (addTds.length-1); i++){
                        console.log(i)
                        addTds.eq(i).val("")
                    }
                    fnLoadHomeData('add')
                })

            })
            
            //  删除图书 删除图书按钮 设置 一个
            $('.delorder').click(function () {
                $('.orderlist').show()
                $('.addlist').hide()
                $('.del').show()
                $('.update').hide()
                    // 监听删除按钮
                    $('.del').on('click',function () {
                        result = $(this).siblings().eq(0).children('input').val()
                        $.ajax({
                            url:'/delete_order.html',
                            dataType:'json',
                            type:'delete',
                            data:JSON.stringify({id:result}),
                            success:function(dat){
                                alert(dat.data)
                                
                                fnLoadHomeData('del')
                            }
                        })
                
                });

                
            })
            
            //  修改图书
            $('.updateorder').click(function () {
                $('.orderlist').show()
                $('.addlist').hide()
                $('.del').hide()
                $('.update').show()
                // 监听修改按钮
                $('.update').on('click',function () {
                        var tds = $(this).siblings().children()

                        console.log(tds)
                        console.log(tds.eq(7))
                        dict_data = {
                            "id":tds.eq(0).val(),
                            "count":tds.eq(1).val(),
                            "price":tds.eq(2).val(),
                            "freight":tds.eq(3).val(),
                            "user":tds.eq(4).val(),
                            "status":tds.eq(5).val(),
                            "time":tds.eq(7).val()
                        }
                        $.ajax({
                            url:"/update_order.html",
                            type:"put",
                            dataType:'json',
                            data:JSON.stringify(dict_data),
                            success:function (dat){
                                alert(dat.data)
                                fnLoadHomeData('update')
                            }
                        })
                 })
                
            })
    })   
    