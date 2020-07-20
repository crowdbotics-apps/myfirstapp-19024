import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import Tutorial81708Navigator from '../features/Tutorial81708/navigator';
import NotificationList81680Navigator from '../features/NotificationList81680/navigator';
import Settings81679Navigator from '../features/Settings81679/navigator';
import Settings81671Navigator from '../features/Settings81671/navigator';
import UserProfile81669Navigator from '../features/UserProfile81669/navigator';
import Settings81633Navigator from '../features/Settings81633/navigator';
import Settings81599Navigator from '../features/Settings81599/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {

    //@BlueprintNavigationInsertion
Tutorial81708: { screen: Tutorial81708Navigator },
NotificationList81680: { screen: NotificationList81680Navigator },
Settings81679: { screen: Settings81679Navigator },
Settings81671: { screen: Settings81671Navigator },
UserProfile81669: { screen: UserProfile81669Navigator },
Settings81633: { screen: Settings81633Navigator },
Settings81599: { screen: Settings81599Navigator },

    /** new navigators can be added here */
    SplashScreen: {
      screen: SplashScreen
    }
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
