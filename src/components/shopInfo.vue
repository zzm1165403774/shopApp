<template>
    <div class="shop">
        <img :src="item.imgUrl" class="shop__img"
        >
        <div class="shop__content" :class="{'shop__content':true, 'shop__content--bordered':hideBorder ? false: true }">
          <div class="shop__content__title">{{item.name}}</div>
          <div class="shop__content__tags">
            <span class="shop__content__tag">月售:{{item.sales}}</span>
            <span class="shop__content__tag">起送:{{item.expressLimit}}</span>
            <span class="shop__content__tag">运费:{{item.expressPrice}}</span>
          </div>
          <p class="shop__content__highlight">{{item.slogan}}</p>
        </div>
      </div>
</template>
<style lang="scss" scoped>
.shop{
    display: flex;
    padding: .12rem;
    &__img{
      margin-right: .16rem;
      padding-top: .12rem;
      width: .56rem;
      height: .56rem;
    }
    &__content{
      &--bordered{
        border-bottom: 1px solid #F1F1F1;
      }
      padding-bottom: .12rem;
      flex: 1;
      &__title{
        line-height: .22rem;
        font-size: .16rem;
        color: #333;
      }
      &__tags{
        margin-top: .08rem;
        line-height: .18rem;
        font-size: .13rem;
        color: #333;
      }
      &__tag{
        margin-right: .16rem;
      }
      &__highlight{
        color: #E93B3B;
        line-height: .18rem;
        font-size: .13rem;
        margin: .08rem 0 0 0;
      }
  }
}
</style>
<script>
export default {
  name: 'shopInfo',
  props: ['item', 'hideBorder']
}
</script>
