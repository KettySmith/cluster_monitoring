(function () {
    $(window).scroll(function () {
        //$(this).offset().top    动画元素顶部离页面顶部的距离
        //$(window).height()      可视化区域的高度
        let winTop = $(window).scrollTop()    //当前可视区域顶部离页面顶部的距离
        // 当前元素距离html的距离 , 如果小于 屏幕滚动的距离 + 屏幕高度 * (在屏幕%几显示动画)
        // 当屏幕滚动到 大于 当前元素的位置时候 , 添加动画
        if ($('.learn-bk').offset().top < winTop + $(window).height() * 0.85) {
            $('.learn-bk').addClass('new')
        } else if ($('.learn-bk').offset().top - $(window).height() >= winTop) {
            $('.learn-bk').removeClass('new')
        }
        if ($('.learn-btn-animate').offset().top < winTop + $(window).height() * 0.85) {
            $('.learn-btn-animate').addClass('learn-btn-new')
        } else if ($('.learn-btn-animate').offset().top - $(window).height() >= winTop) {
            $('.learn-btn-animate').removeClass('learn-btn-new')
        }
        if ($('.recognize-btn').offset().top < winTop + $(window).height() * 0.8) {
            $('.recognize-btn').addClass('recognize-btn-new')
        } else if ($('.recognize-btn').offset().top - $(window).height() >= winTop) {
            $('.recognize-btn').removeClass('recognize-btn-new')
        }
        if ($('.re-left-up').offset().top < winTop + $(window).height() * 0.8) {
            $('.re-left-up').addClass('recognize-btn-new')
        } else if ($('.re-left-up').offset().top - $(window).height() >= winTop) {
            $('.re-left-up').removeClass('recognize-btn-new')
        }
        if ($('.discuss-area').offset().top < winTop + $(window).height() * 0.7) {
            $('.discuss-area').addClass('discuss-area-new')
        } else if ($('.discuss-area').offset().top - $(window).height() >= winTop) {
            $('.discuss-area').removeClass('discuss-area-new')
        }
        if ($('.medicine-area').offset().top < winTop + $(window).height() * 0.7) {
            $('.medicine-area').addClass('medicine-area-new')
        } else if ($('.medicine-area').offset().top - $(window).height() >= winTop) {
            $('.medicine-area').removeClass('medicine-area-new')
        }
        if ($('.font-info').offset().top < winTop + $(window).height() * 0.8) {
            $('.font-info').addClass('font-info-new')
        } else if ($('.font-info').offset().top - $(window).height() >= winTop) {
            $('.font-info').removeClass('font-info-new')
        }
    })
})();

(function info(ele) {
    $(window).scroll(function () {
        //$(this).offset().top    动画元素顶部离页面顶部的距离
        //$(window).height()      可视化区域的高度
        let winTop = $(window).scrollTop()    //当前可视区域顶部离页面顶部的距离
        $(ele).each(function () {
            // 当前元素距离html的距离 , 如果小于 屏幕滚动的距离 + 屏幕高度 * (在屏幕%几显示动画)
            // 当屏幕滚动到 大于 当前元素的位置时候 , 添加动画
            if ($(this).offset().top < winTop + $(window).height() * 0.9) {
                $(this).addClass('font-new')
            } else if ($(this).offset().top - $(window).height() >= winTop) {
                $(this).removeClass('font-new')
            }
        })
        if( $(window).scrollTop() >= 1000){
            // 当窗口的scrollTop >=1000时  让盒子出现
            $('.bottom-float').removeClass("backTop-hidden")
        }else{
            $('.bottom-float').addClass("backTop-hidden");          //否则隐藏
        }
    })
})('.info-area0,.info-area1,.info-area2,.info-area3');


$(document).ready(function (){
    $('.header').load("../html/header.html");
    window.global={
        telephone:"",
        id:"",
    }
})
let WIDTH = document.documentElement.clientWidth;
let HEIGHT = document.documentElement.clientHeight;
// console.log(WIDTH)
// console.log(HEIGHT)
document.documentElement.style.setProperty("--HEIGHT_VIEW", HEIGHT+"px")
document.documentElement.style.setProperty("--WIDTH_VIEW", WIDTH+"px")


let app = new Vue({
    el:"#app",
    data() {
        return {
            car_height:document.documentElement.clientHeight + "px",
            
            
            carousel_content:{},

          
        }
    },
    methods:{
       
        delHandleMouseEnter() {
            this.$refs.carousel.handleMouseEnter = () => { };
        },
        changeCar(e){
            let index = parseInt(e)
            this.carousel_content = this.carousel_list[index];
        },

        handbackTop(){
            document.documentElement.scrollTop = 0;
        }
    },
    mounted(){
        this.$refs.carousel.handleMouseEnter = () => { };
        this.carousel_content = this.carousel_list[0];
    }
})



