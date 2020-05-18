<template>
  <div>
    <div>Controls</div>
    <div>
      <table>
        <tr>
          <th>Device name</th>
          <th>Name</th>
          <th>Pin number</th>
          <th>Action</th>
          <th>State</th>
        </tr>
        <tr v-for="(control, controlIndex) in controls" :key="controlIndex">
          <td>{{ control.device_name }} </td>
          <td>{{ control.name }} </td>
          <td>{{ control.pin_number }} </td>
          <td>{{ control.state }} </td>
          <td><button id="show-modal" @click="openModal(control)">Turn On</button></td>
        </tr>
      </table>
      <Modal v-if="showModal" :control-id="controlId" :control-name="controlName" @close="closedSuggestionModal()" />
    </div>
  </div>
</template>
<script>
import { getDevicesGet, getControlsGet } from '../fetch.service';
import Modal from './Modal.vue';

export default {
  name: 'Devices',
  components: {
    Modal,
  },
  data() {
    return {
      devices: [],
      controls: [],
      showModal: false,
      controlId: null,
      controlName: '',
    };
  },
  mounted() {
    this.getDevices();
    this.getControls();
  },
  methods: {
    getDevices() {
      getDevicesGet()
        .then((x) => {
          this.devices = x;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getControls() {
      getControlsGet()
        .then((x) => {
          this.controls = x;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    openModal(control) {
      this.controlId = control.id;
      this.controlName = control.name;
      this.showModal = true;
    },
    closedSuggestionModal() {
      this.showModal = false;
    },
  },
};
</script>
<style>
table, th, td {
  border: 1px solid black;
}
</style>
