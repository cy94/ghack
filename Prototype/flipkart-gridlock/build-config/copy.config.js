const copyConfig = require('@ionic/app-scripts/config/copy.config');

copyConfig.copySimplFonts = {
  src: '{{ROOT}}/node_modules/simpl-fonts/dist/fonts/**/*',
  dest: '{{WWW}}/fonts/'
};

module.exports = copyConfig;
