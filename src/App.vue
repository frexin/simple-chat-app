<template>
    <div id="app" class="chat-container">
        <msg-history :messages="messages" />
        <msg-form v-on:formSubmit="handleNewMessage" />
    </div>
</template>

<script>
    import MessagesHistory from './components/MessagesHistory.vue'
    import Form from "./components/Form.vue";

    export default {
        name: 'app',
        data: () => {
            return {
                'messages' : [
                    {'author': 'Joffrey', 'text': 'Brilliant', 'date': '10 Mar, 2018'},
                    {'author': 'NINJA', 'text': 'Great resource, thanks bro', 'date': '10 Mar, 2018, 09:55'},
                    {'author': 'I am mister', 'text': 'Thanks peter', 'date': '10 Mar, 2018, 10:19'},
                    {'author': 'Patricia', 'text': 'Sounds good to me', 'date': '10 Mar, 2018, 10:32'},
                ]
            }
        },
        components: {
            'msg-history': MessagesHistory,
            'msg-form': Form
        },
        methods: {
            handleNewMessage: function(msg) {
                this.messages.push(msg);
            }
        }
    }
</script>

<style>
    #app {
        font-size: 12px;
        font-family: Tahoma, sans-serif;
        color: #000;
    }

    .chat-container {
        margin: 0 auto;
        width: 360px;
        border: 1px solid black;
    }
</style>
