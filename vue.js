<script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.js"></script>
<script>
  Vue.component('diff-viewer', {
    template: `
      <div>
        <h1>Diff Viewer</h1>
        
            <table class="diff" summary="Legends">
        <tr> <th colspan="2"> Legends </th> </tr>
        <tr> <td> <table border="" summary="Colors">
                      <tr><th> Colors </th> </tr>
                      <tr><td class="diff_add">&nbsp;Added&nbsp;</td></tr>
                      <tr><td class="diff_chg">Changed</td> </tr>
                      <tr><td class="diff_sub">Deleted</td> </tr>
                  </table></td>
             <td> <table border="" summary="Links">
                      <tr><th colspan="2"> Links </th> </tr>
                      <tr><td>(f)irst change</td> </tr>
                      <tr><td>(n)ext change</td> </tr>
                      <tr><td>(t)op</td> </tr>
                  </table></td> </tr>
    </table>
       
      </div>
    `,
    mounted() {
      // Get references to the change elements in the generated table
      this.changeElements = Array.from(document.querySelectorAll('.diff_add, .diff_chg, .diff_sub'));
    },
    methods: {
      handleFirstChange() {
        const firstChangeElement = document.querySelector('.diff_add, .diff_chg, .diff_sub');
        if (firstChangeElement) {
          firstChangeElement.scrollIntoView({ behavior: 'smooth' });
        }
      },
      handleTop() {
        const tableElement = document.querySelector('table');
        if (tableElement) {
          tableElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      },
      handleNextChange() {
  if (this.changeElements.length > 0) {
    const currentIndex = this.currentChangeIndex || 0;
    const nextIndex = (currentIndex + 1) % this.changeElements.length;

    this.changeElements[nextIndex].scrollIntoView({ behavior: 'smooth' });
    this.currentChangeIndex = nextIndex;
  }
}
,
      handleKeyDown(event) {
        switch (event.key) {
          case 'f':
            this.handleFirstChange();
            break;
          case 't':
            this.handleTop();
            break;
          case 'n':
            this.handleNextChange();
            break;
        }
      },
    },
    data() {
      return {
        currentChangeIndex: 0,
        changeElements: [],
      };
    },
    mounted() {
      document.addEventListener('keydown', this.handleKeyDown);
    },
    beforeUnmount() {
      document.removeEventListener('keydown', this.handleKeyDown);
    },
  });

  new Vue({
    el: '#app',
  });
</script>