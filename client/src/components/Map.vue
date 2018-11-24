<template>
  <div id="game">
    <gmap-map
      :center="{lat:currentLocation.lat, lng:currentLocation.lng}"
      :options="{disableDefaultUI:true}"
      :zoom="15"
      style="width: 100%; height: 100%;"
    >
      <gmap-marker
        :key="index"
        v-for="(m, index) in markers"
        :position="m.position"
        :clickable="false"
        :draggable="false"
        :icon="m.icon"
        :animation="m.animation"
      ></gmap-marker>
      <gmap-circle
        :center="{lat: 60.184, lng: 24.827}"
        :radius="550"
      ></gmap-circle>
    </gmap-map>
    <div id="over-the-map" style="position: absolute; top: 10%; right: 5%; z-index: 99; color: orange; font-size: 26px">
      <b>Score 2500</b>
    </div>
  </div>
</template>

<script>
  import * as VueGoogleMaps from 'vue2-google-maps'
  import Vue from 'vue'

  Vue.use(VueGoogleMaps, {
    load: {
      key: 'AIzaSyD1fZBSVyXMQysg9yaDWclj5uqvHYcudt0'
      // libraries: 'places', //// If you need to use place input
    },
    mounted: function () {
      this.geolocation()
    },
    methods: {
      geolocation: function () {
        navigator.geolocation.getCurrentPosition((position) => {
          this.currentLocation = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
          }
        })
      }
    }
  });

  export default {
    name: 'Map',
    data () {
      return {
        currentLocation: {lat: 60.186864, lng: 24.821758},
        markers: [
          {
            position: {lat: 60.184, lng: 24.827},
            icon: '../assets/crazylabbus.png'
          }
        ]
      }
    }
  }
</script>


<style scoped>
#game {
  height: 100%;
  width: 100%;
}
</style>
