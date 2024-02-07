var demoTrigger = document.querySelector('.demo-trigger');
var paneContainer = document.querySelector('.detail');

new Drift(demoTrigger, {
  paneContainer: paneContainer,
  inlinePane: false,
});