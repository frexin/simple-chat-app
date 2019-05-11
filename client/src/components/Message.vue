<template>
    <li class="msg" v-bind:class="{mine: mine}">
        <div class="author">{{ author }}</div>
        <div class="msg-text">{{ text }}</div>
        <div class="msg-date">{{ date }}</div>
    </li>
</template>

<script>
    export default {
        name: "message",
        props: ['author', 'text', 'date', 'mine'],
    }
</script>

<style scoped>
    li.msg {
        display: block;
        padding: 10px;
        margin-bottom: 15px;

        background-color: #DCF8C6;
        border-radius: 5px;
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.25);
        font-size: 13px;
    }

    li.msg:nth-child(2n) {
        background-color: #FFFFFF;
    }

    li.msg.mine {
        background-color: #f8c5d2;
    }

    .author {
        margin-bottom: 5px;
        font-weight: bold;
        color: #3740a7;
    }

    .msg-text {
        font-size: 14px;
    }

    .msg-date {
        margin-top: 5px;
        font-size: 11px;
        color: #4c4d51;
        text-align: right;
    }
</style>
