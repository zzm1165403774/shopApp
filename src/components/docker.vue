<template>
    <div class="docker">
    <span v-for="(item, index) in dockerList"
    :key="item.icon"
    :class="{'docker__item':true, 'docker__item--active': index === currentIndex}"
    class="docker__item">
      <router-link :to="item.to">
      <div class="iconfont" v-html="item.icon"></div>
      <div class="docker__title">{{item.text}}</div>
      </router-link>
    </span>
  </div>
</template>

<script>
export default {
  name: 'Docker',
  props: ['currentIndex'],
  setup () {
    const dockerList = [
      { icon: '&#xe6a2;', text: '首页', to: { name: 'Home' } },
      { icon: '&#xe638;', text: '购物车', to: { name: 'CartList' } },
      { icon: '&#xe60c;', text: '订单', to: { name: 'OrderList' } },
      { icon: '&#xe60d;', text: '我的', to: { name: 'User' } }
    ]
    return { dockerList }
  }
}
</script>

<style lang="scss" scoped>
.docker{
  color: #333;
  display: flex;
  position: fixed;
  box-sizing: border-box;
  padding: 0 .18rem;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 0.49rem;
  border-top: .01rem solid #F1F1F1;
  background: white;
  &__item{
    flex: 1;
    text-align: center;
    .iconfont{
    margin: 0.07rem 0  0.02rem 0;
    font-size: .18rem;
    }
    a{
      color:#333;
      text-decoration: none;
    }
    &--active{
      a{
        color: #1FA4FC;
      }
    }
  }
  &__title{
  font-size: .2rem;
  transform: scale(0.5,0.5);
  transform-origin: center top;
  }
}
</style>
