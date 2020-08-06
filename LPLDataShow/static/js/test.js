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
                            color: '#57617B'
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
                      "fontsize":"16"
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