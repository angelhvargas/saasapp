const React = require('react');
const { createDevTools } = require('@redux-devtools/core');
const LogMonitor = require('@redux-devtools/log-monitor').default;
const DockMonitor = require('@redux-devtools/dock-monitor').default;
// const SliderMonitor = require('@redux-devtools/slider-monitor').default;

const REDUX_DEV_TOOLS_VISIBLE = true;

const DevTools = createDevTools(
  <DockMonitor toggleVisibilityKey='ctrl-h'
               changePositionKey='ctrl-q'
               changeMonitorKey='ctrl-m'>
    <LogMonitor />
    {<SliderMonitor keyboardEnabled />}
  </DockMonitor>
);

module.exports = DevTools;
