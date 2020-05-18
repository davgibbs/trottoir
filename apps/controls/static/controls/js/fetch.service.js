const axios = require('axios');

axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';


function getDevicesGet(params) {
  const url = '/devices-api/devices';
  return axios.get(url, params)
    .then((x) => x.data);
}

function getControlsGet(params) {
  const url = '/controls-api/controls';
  return axios.get(url, params)
    .then((x) => x.data);
}

function turnOnPost(params) {
  const url = '/app/update-control-state';
  return axios.post(url, params)
    .then((x) => x.data);
}

function doConsole(params) {
  console.log(params);
}


export { getDevicesGet, getControlsGet, turnOnPost, doConsole };
