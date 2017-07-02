import { NgModule } from '@angular/core';
import { IonicApp, IonicModule } from 'ionic-angular';
import { MyApp } from './app.component';
import { AboutPage } from '../pages/about/about.page';

import { TabsPage } from '../pages/tabs/tabs';
import {CouponsPage} from '../pages/coupons/coupons.page';
import {HistoryPage} from '../pages/history/history.page';
import {LeaderBoardPage} from '../pages/leaderboard/leaderboard.page';

import { ChartModule } from 'angular2-highcharts';


declare var require: any;
@NgModule({
  declarations: [
    MyApp,
    AboutPage,
   
    TabsPage,
   
    CouponsPage,
    LeaderBoardPage,
    HistoryPage
  ],
  imports: [
    IonicModule.forRoot(MyApp),ChartModule.forRoot(require('highcharts'),require('highcharts/highcharts-more'),require('highcharts/modules/solid-gauge'))
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    AboutPage,
   
    TabsPage,
   
    CouponsPage,
    LeaderBoardPage,
    HistoryPage
  ],
  providers: []
})
export class AppModule {}
