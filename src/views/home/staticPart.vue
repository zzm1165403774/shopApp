<template>
    <div class="position">
      <span class="iconfont  position__icon">&#xe614;</span>
      天津理工大学8号学生公寓325室
      <span class="iconfont position__notice">&#xe887;</span>
    </div>
    <div class="search">
      <span class="iconfont">&#xe60a;</span>
      <input type="text" value="在此搜索" class="search__input">
    </div>
    <div class="banner">
      <img class="banner__img"
      src="http://www.dell-lee.com/imgs/vue3/banner.jpg"
       />
    </div>
    <div class="icons">
      <div
       class="icons__item"
       v-for="(item, index) in icons"
       :key="index"
      >
        <img
         class="icons__item__img"
         :src="item.imgUrl"
        >
        <p class="icons__item__desc">{{item.desc}}</p>
      </div>
    </div>
    <div class="gap"></div>
</template>

<script>
export default {
  name: 'staticPart',
  setup () {
    const icons = [{
      imgUrl: 'http://www.dell-lee.com/imgs/vue3/超市.png',
      desc: '超市便利'
    }, {
      imgUrl: 'http://www.dell-lee.com/imgs/vue3/菜市场.png',
      desc: '菜市场'
    }, {
      imgUrl: 'http://www.dell-lee.com/imgs/vue3/水果店.png',
      desc: '水果店'
    }, {
      imgUrl: 'http://www.dell-lee.com/imgs/vue3/鲜花.png',
      desc: '鲜花绿植'
    }, {
      imgUrl: 'http://www.dell-lee.com/imgs/vue3/医药健康.png',
      desc: '医药健康'
    }, {
      imgUrl: 'http://www.dell-lee.com/imgs/vue3/家居.png',
      desc: '家居时尚'
    }, {
      imgUrl: 'http://www.dell-lee.com/imgs/vue3/蛋糕.png',
      desc: '烘培蛋糕'
    }, {
      imgUrl: 'http://www.dell-lee.com/imgs/vue3/签到.png',
      desc: '签到'
    }, {
      imgUrl: 'http://www.dell-lee.com/imgs/vue3/大牌免运.png',
      desc: '大牌免运'
    }, {
      imgUrl: 'http://www.dell-lee.com/imgs/vue3/红包.png',
      desc: '红包套餐'
    }]
    return { icons }
  }
}
</script>

<style lang="scss" scoped>
@import '../../style/mixins.scss';
.banner{
  height: 0;
  overflow: hidden;
  padding-bottom: 25.4%;
  &__img{
    width: 100%;
  }
}
.position{
  color: #333;
  padding: .16rem 0;
  margin-right: .35rem;
  line-height: .22rem;
  font-size: .16rem;
  @include ellipsis;
  .position__icon{
    // margin-right: .08rem;
    position: relative;
    top: -.01rem;
    font-size: .2rem;
  }
  .position__notice{
    position: absolute;
    right: .18rem;
    top: .17rem;
    font-size: .2rem;
  }
}
.search{
  margin-bottom: .12rem;
  line-height: .32rem;
  background: #F5F5F5;
  color: #6e5252;
  border-radius: .16rem;
  font-size: .14rem;
  .iconfont{
    padding: 0 .12rem 0 .16rem;
    display: inline-block;
    font-size: .16rem;
  }
  &__input{
    border: hidden;
    width: 80%;
    height: 100%;
    background: #F5F5F5;
    outline: medium;
  }
}
.icons{
  display: flex;
  flex-wrap: wrap;
  margin-top: .16rem;
  &__item{
    width: 20%;
    &__img{
      display: block;
      width: .4rem;
      height: .4rem;
      margin: 0 auto;
    }
    &__desc{
      margin: .06rem 0 .16rem 0;
      text-align: center;
      color: #333;
    }
  }
}
</style>
