<template>
  <div>
    <p>Welcome to the Jol Jardin platform</p>
    <div>
      <Devices />
    </div>
  </div>
</template>
<script>
import joljardinImage from '../img/jol-jardin.png';
import Devices from './components/Devices.vue';

export default {
  name: 'App',
  components: {
    Devices,
  },
  data() {
    return {
      image: joljardinImage,
    };
  },
};
</script>
<style>
</style>
