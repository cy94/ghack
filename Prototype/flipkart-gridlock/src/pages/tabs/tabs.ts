import { Component } from '@angular/core';


import { AboutPage } from '../about/about.page';

import {CouponsPage} from '../coupons/coupons.page';
import {LeaderBoardPage} from '../leaderboard/leaderboard.page';
import {HistoryPage} from '../history/history.page';

@Component({
  templateUrl: 'tabs.html'
})
export class TabsPage {
  // this tells the tabs component which Pages
  // should be each tab's root Page
  tab1Root: any = LeaderBoardPage;
  tab2Root: any = AboutPage;
  tab3Root: any = HistoryPage;
  tab4Root: any = CouponsPage;  

  constructor() {
      
  }
}
