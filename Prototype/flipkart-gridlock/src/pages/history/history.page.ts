import { Component } from '@angular/core';

import { NavController, AlertController } from 'ionic-angular';


@Component({
    selector: 'page-history',
    styles: [`
      chart {
        display: block;
      }
    `],
    templateUrl: 'history.page.html'
})
export class HistoryPage {
    chart: any;
    pointChartOptions: Object;
    pointsGuageOptions: Object;
    

    saveChart(chart) {
        this.chart = chart;
    }

    onPointSelect(point) {
        //alert(`${point.y} is selected`);
    }
    onSeriesHide(series) {
        //alert(`${series.name} is selected`);
    }
    constructor(public navCtrl: NavController, public alertController: AlertController) {

        this.pointChartOptions = {
            title : { text : 'Trends' },
            xAxis: {
       // categories: ['Jun 25', 'Jun 26', 'Jun 27', 'Jun 28', 'Jun 29', 'Jun 28', 'Jun 29', 'Jun 30', 'Jul 1', 'Jul 2']
       categories: ['-9', '-8', '-7', '-6', '-5', '-4', '-3', '-2', '-1', 'Today']
    },
            series: [{
                name: 'Points',
                data: [0, 23, 38, 44,41,56,64,59,71,87]
            }]
        };

        this.pointsGuageOptions = {

              chart: {
                type: 'solidgauge'
              },

              title: "Temperature",

            /*  pane: {
                center: ['50%', '85%'],
                size: '60%',
                startAngle: -90,
                endAngle: 90,
                background: {

                  innerRadius: '60%',
                  outerRadius: '100%',
                  shape: 'arc'
                }
              },*/

              tooltip: {
                enabled: false

              },
              yAxis: {
                stops: [
                  
                  [0.1, '#DF5353'], // green
                  [0.5, '#DDDF0D'], // yellow
                  [0.9, '#55BF3B'] // red
                ],
                lineWidth: 0,
                minorTickInterval: null,
                tickAmount: 2,
                title: {
                  y: -100,
                  text: 'Current Score meter'
                },
                labels: {
                  y: 16
                },
                min: 0,
                max: 100
              },
              plotOptions: {
                solidgauge: {
                  dataLabels: {
                    y: 5,
                    borderWidth: 0,
                    useHTML: true
                  }
                }
              },

              series: [
                {
                  name: 'score',
                  data: (function () {
                    var val = [];

                    //val.push(+item.sensor.temp*eval_formula);
                    val.push(87);
                    //val.push(+this.device.temp);

                    return val;
                  }()),
                  dataLabels: {
                    format: '<div style="text-align:center"><span style="font-size:25px;color:' +
                    ('black') + '">{y}</span>' +
                    '<span style="font-size:12px;color:black"></span></div>'
                  }

                }]
            };

    }



}