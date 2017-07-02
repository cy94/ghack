import { Component } from '@angular/core';

import { NavController } from 'ionic-angular';

@Component({
  selector: 'page-about',
  templateUrl: 'about.page.html'
})
export class AboutPage {

  pointsGuageOptions: Object;

  constructor(public navCtrl: NavController) {
     this.pointsGuageOptions = {

              chart: {
                type: 'solidgauge'
              },

              title: "Points",

         pane: {
                center: ['30%', '60%'],
               size: '60%',
             /*   startAngle: -90,
                endAngle: 90,
               
                background: {
                backgroundColor:'#ffcc66',
                  innerRadius: '60%',
                  outerRadius: '100%',
                  shape: 'full'
                }*/
              },

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
