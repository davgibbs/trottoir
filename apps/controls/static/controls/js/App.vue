<template>
  <div>
    <p>Welcome to the Trottoir Platform</p>
    <img :src="image">
  </div>
</template>
<script>
import footpathImage from '../img/footpath.jpg';

export default {
  name: 'App',
  data() {
    return {
      image: footpathImage,
    };
  },
};
</script>
<style>
</style>
