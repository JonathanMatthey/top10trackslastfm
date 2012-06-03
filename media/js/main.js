$(function () {
    var chart;
    var chart2;
    var chart3;

    $(document).ready(function() {
        chart = new Highcharts.Chart({
            chart: {
                renderTo: 'chart_container',
                type: 'line',
                marginRight: 130,
                marginBottom: 40
            },
            title: {
                text: 'Total Listeners of Top 10 Tracks by Week',
                x: -20 //center
            },
            subtitle: {
                text: 'Source: last.fm',
                x: -20
            },
            xAxis: {
                categories: all_weeks,
                title: {
                    text: 'week',
                    align: 'high'
                },

            },
            yAxis: {
                title: {
                    text: 'Listeners'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#D51007'
                }]
            },
            tooltip: {
                formatter: function() {
                        return '<b>'+ this.series.name +'</b><br/>'+
                        this.x +': '+ this.y +'°C';
                }
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'top',
                x: -10,
                y: 100,
                borderWidth: 0
            },
            series: [{
                name: 'Total Listeners',
                data: total_listeners_series,
                track_id: 1,
                color: '#D51007'
            }]
        });

        chart2 = new Highcharts.Chart({
            chart: {
                renderTo: 'chart_container2',
                type: 'bar'
            },
            title: {
                text: 'Total Listeners for Top 10 Artists'
            },
            subtitle: {
                text: 'Source: last.fm'
            },
            xAxis: {
                categories: artist_listeners_x_axis,
                title: {
                    text: null
                }
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'listeners',
                    align: 'high'
                }
            },
            tooltip: {
                formatter: function() {
                    return ''+
                        this.series.name +': '+ this.y +' ';
                }
            },
            plotOptions: {
                bar: {
                    dataLabels: {
                        enabled: true
                    }
                }
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'top',
                x: -100,
                y: 100,
                floating: true,
                borderWidth: 1,
                backgroundColor: '#FFFFFF',
                shadow: true
            },
            credits: {
                enabled: false
            },
                series: [{
                name: 'Listeners',
                data: artist_listeners_series,
                color: '#D51007'
            }]
        });

        chart3 = new Highcharts.Chart({
            chart: {
                renderTo: 'chart_container3',
                type: 'line',
                marginRight: 130,
                marginBottom: 40
            },
            title: {
                text: 'Top 10 Listener Distribution',
                x: -20 //center
            },
            subtitle: {
                text: 'Source: last.fm',
                x: -20
            },
            xAxis: {
                categories: [1,2,3,4,5,6,7,8,9,10],
                title: {
                    text: 'Position',
                    align: 'high'
                }
            },
            yAxis: {
                title: {
                    text: 'Listeners'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#D51007'
                }]
            },
            tooltip: {
                formatter: function() {
                        return '<b>'+ this.series.name +'</b><br/>'+
                        this.x +': '+ this.y +'°C';
                }
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'top',
                x: -10,
                y: 100,
                borderWidth: 0
            },
            series: [{
                name: 'Listeners',
                data: billboard_listeners_series,
                track_id: 1,
                color: '#D51007'
            }]
        });


        $("select#year, select#week").live("change keyup", function () {
            $("#form1").submit();
        });


        $("select#week").val(qweek);

        $("#easter-egg").click(function(event){
            event.preventDefault();
            $('#chart_container, #chart_container3, #chart_container2').toggle();
            $('#ee1, #ee2, #ee3').toggle();
        });

    });




});