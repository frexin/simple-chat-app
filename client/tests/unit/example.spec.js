import {mount, shallowMount} from '@vue/test-utils'
import App from '@/App.vue'

describe('HelloWorld.vue', () => {
  it('renders props.msg when passed', () => {
    const wrapper = mount(App);

    expect(wrapper.contains('div.msg-history')).toBe(true);
  })
});
