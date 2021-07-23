<template>
  <div class="wrapper">
      <StaticPart />
      <Nearby />
  </div>
  <Docker :currentIndex ="0" />
</template>

<script>
import StaticPart from './staticPart'
import Nearby from './nearby'
import Docker from '../../components/docker'
export default {
  name: 'home',
  components: { StaticPart, Nearby, Docker }
}
</script>

<style lang="scss" scoped>
.wrapper{
  position: absolute;
  left: 0;
  top: 0;
  bottom: .5rem;
  right: 0;
  padding: 0 .18rem ;
  overflow-y: auto;
  // background: blue;
}
</style>
