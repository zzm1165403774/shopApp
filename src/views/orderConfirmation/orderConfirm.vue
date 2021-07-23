<template>
    <div class="wrapper">
        <Top />
        <Products />
        <Order />
    </div>
</template>

<script>
import Top from './Top'
import Products from './Products'
import Order from './Order'

export default {
  components: { Top, Products, Order },
  name: 'orderConfirm'
}
</script>

<style lang="scss" scoped>
@import '../../style/mixins.scss';
.wrapper{
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0;
    top: 0;
    background-color: #fff;
    overflow-y: scroll;
}
</style>
