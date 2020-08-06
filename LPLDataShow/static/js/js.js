 $(window).load(function(){  
             $(".loading").fadeOut()
            })  
$(function () {
    echarts_1();
	echarts_2();
	echarts_3();
	echarts_4();
	echarts_5();
	homedata();
	wingstop5();
	heropick60();
function echarts_1() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart1'));
        option = {
                    tooltip : {
                        trigger: 'item',
                        formatter: "{b} : {c} ({d}%)"
                    },
                    legend: {
                        right:0,
                        top:30,
                        height:160,
                        itemWidth:10,
                        itemHeight:10,
                        itemGap:10,
                        textStyle:{
                            color: 'rgba(255,255,255,.6)',
                            fontSize:12
                        },
                        orient:'vertical',
                        data:['RNG','DOM','WE','JDG','FPX']
                    },
                   calculable : true,
                    series : [
                        {
                            name:' ',
							color: ['#62c98d', '#2f89cf', '#4cb9cf', '#53b666', '#62c98d', '#205acf', '#c9c862', '#c98b62', '#c962b9', '#7562c9','#c96262','#c25775','#00b7be'],	
                            type:'pie',
                            radius : [30, 70],
                            center : ['35%', '50%'],
                            roseType : 'radius',
                            label: {
                                normal: {
                                    show: true
                                },
                                emphasis: {
                                    show: true
                                }
                            },

                            lableLine: {
                                normal: {
                                    show: true
                                },
                                emphasis: {
                                    show: true
                                }
                            },

                            data:[
                                {value:10, name:'RNG'},
                                {value:5, name:'DOM'},
                                {value:15, name:'WE'},
                                {value:25, name:'JDG'},
                                {value:20, name:'FPX'},
                      
                            ]
                        },
                    ]
                };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }
function echarts_2() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart2'));

        option = {
            tooltip: {
                trigger: 'item',
               formatter: "{b} : {c} ({d}%)"
            },
            legend: {
			
				top:'15%',
                data: ['LNG\nLight', 'RNG\nXLB', 'FPX\nDoinb', 'IG\nTheShy', 'TES\nknight'],
                icon: 'circle',
                textStyle: {
                    color: 'rgba(255,255,255,.6)',
                }
            },
            calculable: true,
            series: [{
                name: '',
				color: ['#62c98d', '#2f89cf', '#4cb9cf', '#53b666', '#62c98d', '#205acf', '#c9c862', '#c98b62', '#c962b9','#c96262'],	
                type: 'pie',
                //起始角度，支持范围[0, 360]
                startAngle: 0,
                //饼图的半径，数组的第一项是内半径，第二项是外半径
                radius: [51, 100],
                //支持设置成百分比，设置成百分比时第一项是相对于容器宽度，第二项是相对于容器高度
                center: ['50%', '45%'],
				
                //是否展示成南丁格尔图，通过半径区分数据大小。可选择两种模式：
                // 'radius' 面积展现数据的百分比，半径展现数据的大小。
                //  'area' 所有扇区面积相同，仅通过半径展现数据大小
                roseType: 'area',
                //是否启用防止标签重叠策略，默认开启，圆环图这个例子中需要强制所有标签放在中心位置，可以将该值设为 false。
                avoidLabelOverlap: false,
                label: {
                    normal: {
                        show: true,
                      //  formatter: '{c}辆'
                    },
                    emphasis: {
                        show: true
                    }
                },
                labelLine: {
                    normal: {
                        show: true,
                        length2: 1,
                    },
                    emphasis: {
                        show: true
                    }
                },
                data: [
                    {value: 1,name: 'LNG\nLight',},
                    {value: 4,name: 'RNG\nXLB',},
                    {value: 5,name: 'FPX\nDoinb',},
                    {value: 6,name: 'IG\nTheShy',},
                    {value: 9,name: 'TES\nknight',},
         
                   

                    {value: 0, name: "",label: {show: false},labelLine: {show: false}},
                    {value: 0, name: "",label: {show: false},labelLine: {show: false}},
                    {value: 0, name: "",label: {show: false},labelLine: {show: false}},
                    {value: 0, name: "",label: {show: false},labelLine: {show: false}},
                    {value: 0, name: "",label: {show: false},labelLine: {show: false}},

                   
                ]
            }]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }
function echarts_3() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart3'));
        var lpl = {};
        $.ajax({
            url:'/memberdata',
            data: {},
            type: 'POST',
            async: false,
            dataType:'json',
            success:function (data) {
                lpl.name = data.name;
                lpl.killsum = data.killsum;
                lpl.assistsum = data.assistsum;
                lpl.diesum = data.diesum;
                myChart.setOption({
                    tooltip: {
		            trigger: 'axis',
		            axisPointer: {
			        lineStyle: {
				color: '#57617B'
			}
		}
	},
	                legend: {

		//icon: 'vertical',
			data: ['总击杀', '总助攻','总死亡'],
        //align: 'center',
       // right: '35%',
		top:'0',
        textStyle: {
            color: "#fff"
        },
       // itemWidth: 15,
       // itemHeight: 15,
        itemGap: 20,
	},
	                grid: {
		left: '0',
		right: '20',
		top:'10',
		bottom: '20',
		containLabel: true
	},
	                xAxis: [{
		type: 'category',
		boundaryGap: false,
		axisLabel: {
			show: true,
			textStyle: {
                           color: 'rgba(255,255,255,1)',
                fontSize:8
                        }
		},
		axisLine: {
			lineStyle: {
				color: 'rgba(255,255,255,.1)'
			}
		},
		data: lpl.name
	},],
	                yAxis: [{
		axisLabel: {
			show: true,
			textStyle: {
                           color: 'rgba(255,255,255,.6)'
                        }
		},
		axisLine: {
			lineStyle: {
				color: 'rgba(255,255,255,.1)'
			}
		},
		splitLine: {
			lineStyle: {
				color: 'rgba(255,255,255,.1)'
			}
		}
	}],
	                series: [{
		name: '总击杀',
		type: 'line',
		smooth: true,
		symbol: 'circle',
		symbolSize: 5,
		showSymbol: false,
		lineStyle: {
			normal: {
				width: 2
			}
		},
		areaStyle: {
			normal: {
				color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
					offset: 0,
					color: 'rgba(24, 163, 64, 0.3)'
				}, {
					offset: 0.8,
					color: 'rgba(24, 163, 64, 0)'
				}], false),
				shadowColor: 'rgba(0, 0, 0, 0.1)',
				shadowBlur: 10
			}
		},
		itemStyle: {
			normal: {
				color: '#cdba00',
				borderColor: 'rgba(137,189,2,0.27)',
				borderWidth: 12
			}
		},
		data: lpl.killsum
	}, {
		name: '总助攻',
		type: 'line',
		smooth: true,
		symbol: 'circle',
		symbolSize: 5,
		showSymbol: false,
		lineStyle: {
			normal: {
				width: 2
			}
		},
		areaStyle: {
			normal: {
				color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
					offset: 0,
					color: 'rgba(39, 122,206, 0.3)'
				}, {
					offset: 0.8,
					color: 'rgba(39, 122,206, 0)'
				}], false),
				shadowColor: 'rgba(0, 0, 0, 0.1)',
				shadowBlur: 10
			}
		},
		itemStyle: {
			normal: {
				color: '#277ace',
				borderColor: 'rgba(0,136,212,0.2)',
				borderWidth: 12
			}
		},
		data: lpl.assistsum
	}, {
		name: '总死亡',
		type: 'line',
		smooth: true,
		symbol: 'circle',
		symbolSize: 5,
		showSymbol: false,
		lineStyle: {
			normal: {
				width: 2
			}
		},
		areaStyle: {
			normal: {
				color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
					offset: 0,
					color: 'rgba(39, 122,206, 0.3)'
				}, {
					offset: 0.8,
					color: 'rgba(39, 122,206, 0)'
				}], false),
				shadowColor: 'rgba(0, 0, 0, 0.1)',
				shadowBlur: 10
			}
		},
		itemStyle: {
			normal: {
				color: '#67E0E3',
				borderColor: 'rgba(10,148,236,0.5)',
				borderWidth: 12
			}
		},
		data: lpl.diesum
	}]
                })
            },
            error:function (msg) {
            console.log(msg);
            alert('系统发生错误!个人击杀数据');
        }
        });
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }
function echarts_4() {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('echart4'));
    var lpl = {};
    $.ajax({
        url:'/wingsvd',
        data: {},
        type: 'POST',
        async: false,
        dataType:'json',
        success: function (data) {
            lpl.name = data.name;
            lpl.victory = data.victory;
            lpl.defeat = data.defeat;
            lpl.winRate = data.winRate;
            myChart.setOption({
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        lineStyle: {
                            color: '#ffffff'
                        }
                    }
                },
                legend: {

                  "data": [
                    {"name": "Victory"},
                    {"name": "Defeat"},
                    {"name": "胜率"}
                  ],
                  "top": "0%",
                  "textStyle": {
                   "color": "rgba(255,255,255,1)",//图例文字
                      "fontSize":"16"
                  }
                },

                xAxis: [
                  {
                    "type": "category",

                    data: lpl.name,
                    axisLine: { lineStyle: {color: "rgba(255,255,255,.1)"}},
                    axisLabel:  { textStyle: {color: "rgb(255,255,255)", fontSize: '16', },
                        },

                    },
                ],
                yAxis: [
                  {
                    "type": "value",
                    "name": "次数",
                    "min": 0,
                    "max": 30,
                    "interval": 10,
                    "axisLabel": {
                      "show": true,

                    },
                    axisLine: {lineStyle: {color: 'rgba(255,255,255,1)'}},//左线色
                    splitLine: {show:true,lineStyle: {color:"rgba(255,255,255,1)"}},//x轴线
                  },
                  {
                    "type": "value",
                    "name": "胜率",
                    "show": true,
                    "axisLabel": {
                      "show": true,

                    },
                      axisLine: {lineStyle: {color: 'rgba(255,255,255,1 )'}},//右线色
                       splitLine: {show:true,lineStyle: {color:"rgba(255,255,255,0.2)"}},//x轴线
                  },
                ],
                grid: {
                  "top": "10%",
                    "right":"30",
                    "bottom":"30",
                    "left":"30",
                },
                series: [
                  {
                    "name": "Victory",

                    "type": "bar",
                    "data": lpl.victory,
                    "barWidth": "auto",
                    "itemStyle": {
                      "normal": {
                        "color": {
                          "type": "linear",
                          "x": 0,
                          "y": 0,
                          "x2": 0,
                          "y2": 1,
                          "colorStops": [
                            {
                              "offset": 0,
                              "color": "#67E0E3"
                            },

                            {
                              "offset": 1,
                              "color": "#67E0E3"
                            }
                          ],
                          "globalCoord": false
                        }
                      }
                    }
                  },
                  {
                    "name": "Defeat",
                    "type": "bar",
                    "data": lpl.defeat,
                    "barWidth": "auto",

                    "itemStyle": {
                      "normal": {
                        "color": {
                          "type": "linear",
                          "x": 0,
                          "y": 0,
                          "x2": 0,
                          "y2": 1,
                          "colorStops": [
                            {
                              "offset": 0,
                              "color": "#FFDB5C"
                            },
                            {
                              "offset": 1,
                              "color": "#FFDB5C"
                            }
                          ],
                          "globalCoord": false
                        }
                      }
                    },
                    "barGap": "0"
                  },
                  {
                    "name": "胜率",
                    "type": "line",
                    "yAxisIndex": 1,

                    "data": lpl.winRate,
                      lineStyle: {
                        normal: {
                            width: 2
                        },
                    },
                    "itemStyle": {
                      "normal": {
                        "color": "#48f593",

                      }
                    },
                    "smooth": true
                  }
                ]
            })
        },
        error:function (msg) {
            console.log(msg);
            alert('系统发生错误!');
        }
    });
    window.addEventListener("resize",function(){
        myChart.resize();
    });
}
function echarts_5() {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('echart5'));
    var lpl = {};
    $.ajax({
        url:'/memberdata',
        data: {},
        type: 'POST',
        async: false,
        dataType:'json',
        success:function (data) {
            lpl.name = data.name;
            lpl.outcount = data.outcount;
            lpl.killsum = data.killsum;
            lpl.assistsum = data.assistsum;
            lpl.diesum = data.diesum;
            myChart.setOption({
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
            }
        },
        legend: {
            data: ['出场次数', '总击杀', '总助攻', '总死亡',],
            textStyle: {
                color: 'skyblue'
            }
        },
        grid: {
            left: '0%',
            right: '4%',
            bottom: '1%',
            containLabel: true
        },
        xAxis: {
            type: 'value',
            axisLine: {lineStyle: {color: 'rgba(255,255,255,1)'}},//左线色
        },
        yAxis: {
            type: 'category',
            axisLine: {lineStyle: {color: 'rgba(255,255,255,1)'}},//左线色
            splitLine: {show:true,lineStyle: {color:"rgba(255,255,255,.1)"}},//x轴线
            data: lpl.name
        },
        series: [
            {
                name: '出场次数',
                type: 'bar',
                stack: '总量',
                itemStyle: {
                    color: '#37A2DA'
                },
                label: {
                    show: false,
                    position: 'insideRight'
                },
                data: lpl.outcount
            },
            {
                name: '总击杀',
                type: 'bar',
                stack: '总量',
                itemStyle: {
                    color: '#67E0E3'
                },
                label: {
                    show: false,
                    position: 'insideRight'
                },
                data: lpl.killsum
            },
            {
                name: '总助攻',
                type: 'bar',
                stack: '总量',
                itemStyle: {
                    color: '#FFDB5C'
                },
                label: {
                    show: false,
                    position: 'insideRight'
                },
                data: lpl.assistsum
            },
            {
                name: '总死亡',
                type: 'bar',
                stack: '总量',
                itemStyle: {
                    color: '#FF9F7F'
                },
                label: {
                    show: false,
                    position: 'insideRight'
                },
                data: lpl.diesum
            },

        ]
            })
        },
        error:function (msg) {
            console.log(msg);
            alert('系统发生错误!个人数据堆叠图');
        }
    });
        // 使用刚指定的配置项和数据显示图表。
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }
function round(elm,data1,data2,clolr,str1,str2,str3) {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById(elm));
	    var v2=data2//胜利
		var v1=data1//战败
		var v3=v1+v2//总消费 
        option = {
            tooltip: {
                trigger: 'item',
            },
            series: [{
		
                type: 'pie',
                radius: ['60%', '70%'],
                color:clolr,
                label: {
                    normal: {
                    position: 'center'
                    }
                },
            data: [{
                value: v2,
                name: str1,
                label: {
                    normal: {
                        formatter: v2 +'',
                        textStyle: {
                            fontSize: 20,
                            color:'#fff',
                        }
                    }
                }
            }, {
                value: v1,
                name: str2,
                label: {
                    normal: {
                        formatter : function (params){
                            return str3
                        },
                        textStyle: {
                            color: '#aaa',
                            fontSize: 12
                        }
                    }
                },
                itemStyle: {
                    normal: {
                        color: 'rgba(255,255,255,.2)'
                    },
                    emphasis: {
                        color: '#fff'
                    }
                },
            }]
            }]
        };
        myChart.setOption(option);
        window.addEventListener("resize",function(){
        myChart.resize();
        });
    }
function KDA(ka,d) {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('zb6'));
        var v1=d//死亡
		var v2=ka//击杀和助攻
option = {
    tooltip: {
        trigger: 'item',
    },
    series: [{

        type: 'pie',
       radius: ['60%', '70%'],
        color:'#FB7293',
        label: {
            normal: {
                position: 'center'
            }
        },
        data: [{
            value: v2,
            name: '击杀和助攻',
            label: {
                normal: {
                    formatter: v2 +'',
                    textStyle: {
                        fontSize: 20,
						color:'#fff',
                    }
                }
            }
        }, {
            value: v1,
            name: '死亡',
            label: {
                normal: {
                 formatter : function (params){
                return 'KDA：'+Math.round( (ka)/d)
            },
                    textStyle: {
                        color: '#aaa',
                        fontSize: 12
                    }
                }
            },
            itemStyle: {
                normal: {
                    color: 'rgba(255,255,255,.2)'
                },
                emphasis: {
                    color: '#fff'
                }
            },
        }]
    }]
};
        myChart.setOption(option);
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }

function wingstop5() {
    $.ajax({
        url:'/wingstop5',
        data: {},
        type: 'POST',
        async: false,
        dataType:'json',
        success:function (data) {
            $("#wingstop5").children('tr').each(function (index,dom) {
                if (index != 0){
                    $(dom).children('td').eq(1).text(data.name[index-1]);
                    $(dom).children('td').eq(2).text(data.outcount[index-1]);
                    $(dom).children('td').eq(3).text(data.winRate[index-1]);
                }
            });
            $("#membertop5").children('tr').each(function (index,dom) {
                if (index != 0){
                    $(dom).children('td').eq(1).text(data.membername[index-1]);
                    $(dom).children('td').eq(2).text(data.memberpost[index-1]);
                    $(dom).children('td').eq(3).text(data.memberkillsum[index-1]);
                }
            })
        },
        error:function (msg) {
            console.log(msg);
            alert('系统发生错误!战队排行榜');
        }
    })


}
function heropick60() {
    $.ajax({
        url:'/heropick',
        data: {},
        type: 'POST',
        async: false,
        dataType:'json',
        success:function (data) {
            var name = data.name;
            var outcount = data.outcount;
            var winrate = data.winrate;
            var picknum = data.picknum;

            $.each(name,function (i,item) {
                $("#heropick").append("<li><p><span>"+ item +"</span><span>"+outcount[i]+"</span><span>"+picknum[i]+"</span><span>"+winrate[i]+"</span></p></li>");
            });
            $('.wrap,.adduser').liMarquee({
                direction: 'up',/*身上滚动*/
                runshort: false,/*内容不足时不滚动*/
                scrollamount: 20/*速度*/
            });
        },
        error:function (msg) {
            console.log(msg);
            alert('系统发生错误!战队排行榜');
        }
    })
}
function homedata() {
    $.ajax({
        url:'/homeround',
        data: {},
        type: 'POST',
        async: false,
        dataType:'json',
        success:function (data) {
            var homename = data.name
            var data1 = data.data1
            var data2 = data.data2

            $("#winratetop").append(homename[0]+"<br>胜率最高");
            $("#killtop").append(homename[1]+"<br>击杀最高");
            $("#ineyetop").append(homename[2]+"<br>插眼最多");
            $("#memberkdatop").append(homename[3]+"<br>KDA最高");
            $("#memberdietop").append(homename[4]+"<br>死亡最多");
            $("#memberkilltop").append(homename[5]+"<br>击杀最多");

            round('zb1',data2[0],data1[0],'#37A2DA','胜利','战败','胜利场数');
	        round('zb2',data2[1],data1[1],'#32C5E9','总击杀','总死亡','总击杀');
	        round('zb3',data2[2],data1[2],'#67E0E3','插眼','排眼','总插眼');
	        round('zb5',data2[4],data1[4],'#FFDB5C','助攻','击杀和助攻','总死亡');
            round('zb4',data2[5],data1[5],'#9FE6B8','击杀','死亡和助攻','总击杀');
            KDA(data1[3],data2[3]);
        },
        error:function (msg) {
            console.log(msg);
            alert('系统发生错误!战队排行榜');
        }
    });


}
})



		
