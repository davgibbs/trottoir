<template>
  <div class="d-flex flex-column justify-content-between">
    <Transition name="modal">
      <div class="modal-mask">
        <div class="modal-container">
          <div class="modal-header">
            <slot name="header">
              Turn on "{{ controlName }}"
            </slot>
            <i class="fas fa-times close-modal-icon pointer" @click="close" />
          </div>
          <div class="modal-body">
            <div class="original-address-row d-flex flex-column">
              <div class="d-flex flex-fill align-items-center pb-1">
                <div v-if="!messageSent">
                  Duration in seconds:
                  <input v-model="duration">
                </div>
                <div v-if="messageSent">
                  Command sent
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer text-right">
            <button v-if="!messageSent" type="button" class="btn btn-green-gd" @click="send">
              Send
            </button>
            <button type="button" class="btn btn-orange-gd" @click="close">
              Close
            </button>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script>
import { turnOnPost } from '../fetch.service';

export default {
  name: 'Modal',
  props: {
    deviceId: {
      default: null,
      type: Number,
    },
    controlId: {
      default: null,
      type: Number,
    },
    controlName: {
      default: '',
      type: String,
    },
  },
  data() {
    return {
      duration: '',
      messageSent: false,
    };
  },
  methods: {
    close() {
      this.$emit('close');
    },
    send() {
      turnOnPost({ deviceId: this.deviceId, controlId: this.controlId, duration: this.duration })
        .then(() => {
          console.log('command sent');
          this.messageSent = true;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};

</script>
<style scoped>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-container {
  max-width: 500px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
  align-items: center;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}

/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}

</style>
