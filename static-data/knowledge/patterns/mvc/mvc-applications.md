---
title: "MVC in Production: Web Frameworks"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Describe the request lifecycle"
  - "Keep models fat, controllers thin"
  - "Organize views and templates"
  - "Test each layer"
prerequisites:
  []
knowledge_refs:
  - "patterns/mvc"
---

# MVC in Production: Web Frameworks

## The Lifecycle

In Rails and Django, a request flows: router -> controller action -> model operations -> view rendering. "Fat model, thin controller" means business rules live in the model (or service objects), and controllers only parse input and orchestrate. Views stay dumb: templates read, never mutate.

```ruby
# Rails-style controller: thin, orchestration only
class OrdersController < ApplicationController
  def create
    order = Order.new(order_params)          # model owns rules
    if order.charge_and_save                # business logic in model
      redirect_to order, notice: "Placed"
    else
      render :new, status: :unprocessable_entity
    end
  end

  private
  def order_params
    params.require(:order).permit(:sku, :qty)   # input parsing only
  end
end
# The model validates, computes totals, and persists; the
# controller never knows business rules.
```

## Where Logic Lives

The classic failure: logic migrates into the controller (fat controllers) or into the view (logic in templates). Service objects and form objects pull orchestration out of controllers; presenters pull formatting out of views. The model layer stays the single home of domain rules.

## Practice: Refactor the Fat Controller

A checkout controller has 200 lines: tax, discount, and inventory rules inline.

**Task 1:** Move tax and discount rules into the model/service layer.

**Task 2:** Move formatting (currency, dates) into a presenter.

**Task 3:** Rewrite the controller to orchestrate only and re-run the tests.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why fat controllers are the MVC failure mode and where the rules should live instead.

**Prompt 2 — Implementation Design:**
> Design a service layer for a checkout: which steps are services, what does the controller keep?

**Prompt 3 — Boundary Testing:**
> A template starts computing discounts. Design the presenter move and the test that guards it.

## Key Takeaways

- The request lifecycle is router -> controller -> model -> view
- Fat models, thin controllers, dumb views
- Service objects keep controllers lean
- Presenters keep formatting out of templates

## Further Reading

- [Ruby on Rails — Action Controller Overview](https://guides.rubyonrails.org/action_controller_overview.html)
- [Django — request/response cycle](https://docs.djangoproject.com/en/stable/intro/tutorial03/)
