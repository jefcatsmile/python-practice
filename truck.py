from car import Car


class truck(Car):
    # 属性を全て初期値でセット
    def __init__(self, model_name, mileage, manufacturer, max_loadings, loadings):
        # 承継クラスの属性は、superを利用して受け渡す
        super().__init__(model_name=model_name, mileage=mileage, manufacturer=manufacturer)
        self._max_loadings = max_loadings
        self._loadings = loadings

    def load(self, weight):
        if weight < 0:
            if self._loadings <= abs(weight):
                print(f"全ての荷物 {self._loadings}t を下ろします")
                self._loadings = 0
            else:
                self._loadings += weight
                print(f"{abs(weight)}t の荷物を下ろします")
        else:
            print(f"{weight}t の荷物を積み込みます")
            self._loadings += weight

        print(f"現在の積載量は、{self._loadings}t です")

        if self._loadings > self._max_loadings:
            print(f"最大積載量{self._max_loadings}をオーバーしています")

if __name__ == '__main__':
    settler = truck('Settler', 10, 'Isuzu', 10, 2)
    settler.load(3)
    print()
    settler.load(-4)
    print()
    settler.load(10)
    print()
    settler.load(-20)
